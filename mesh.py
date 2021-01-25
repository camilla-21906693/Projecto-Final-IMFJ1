"""Mesh class definition"""
# Just import time if we need statistics
import time
import math
import pygame
from vector3 import Vector3
import matrix4


class Mesh:
    """Mesh class.
    Stores a list of polygons to be drawn
    """
    stat_vertex_count = 0
    """Vertex count for statistics. This code that actually tracks the statistics
    is normally commented out for performance reasons (see render method)"""
    stat_transform_time = 0
    """Time spent on vertex transforming for statistics. This code that actually tracks
    the statistics is normally commented out for performance reasons (see render method)"""
    stat_render_time = 0
    """Time spent in rendering for statistics. This code that actually tracks the statistics
    is normally commented out for performance reasons (see render method)"""

    def __init__(self, name="UnknownMesh"):
        """
        Arguments:
            name {str} -- Name of the material, defaults to 'UnknownMesh'
        """
        self.name = name
        """ {str} Name of the mesh"""
        self.polygons = []
        """ {list[list[Vector3]]} List of lists of polygons. A polygon is a closed shape,
        hence the need for a list of lists, if we want more complex shapes."""

    def offset(self, v):
        """
        Offsets this mesh by a given vector. In practice, adds v to all vertex in all polygons
        Arguments:
            v {Vector3} -- Ammount to displace the mesh
        """
        new_polys = []
        for poly in self.polygons:
            new_poly = []
            for p in poly:
                new_poly.append(p + v)
            new_polys.append(new_poly)

        self.polygons = new_polys

    def render(self, screen, clip_matrix, material):
        """
        Renders the mesh.
        Arguments:
            screen {pygame.surface} -- Display surface on which to render the mesh
            clip_matrix {Matrix4} -- Clip matrix to use to convert the 3d local space coordinates
            of the vertices to screen coordinates.
            material {Material} -- Material to be used to render the mesh
            Note that this function has the code that tracks statistics for the vertex count and
            render times, but it is normally commented out, for performance reasons. If you want
            to use the statistics, uncomment the code on this funtion.
        """
        # Convert Color to the pygame format
        c = material.Color.tuple3()
        w = screen.get_width() * 0.5
        h = screen.get_height() * 0.5

        # For all polygons
        for poly in self.polygons:
            # Create the list that will store (temporarily) the transformed vertices
            tpoly = []
            # Uncomment next 2 lines for statistics
            Mesh.stat_vertex_count += len(poly)
            t0 = time.time()
            for v in poly:
                # Multiply vertex it by the clip matrix - This function is slightly faster than doing
                # vout = v * clip_matrix, since it doesn't have to check types or create additional
                # Vector4 objects
                vout = clip_matrix.premultiply_v3(v, 1)

                # Finalize the transformation by converting the point from homogeneous NDC to
                # screen coordinates (divide by w, scale it by the viewport resolution and
                # offset it)
                tpoly.append((w + vout.x / vout.w,
                              h - vout.y / vout.w))

            # Uncomment next line for statistics
            t1 = time.time()

            # Render
            pygame.draw.polygon(screen, c, tpoly, material.line_width)

            # Uncomment next 3 lines for statistics
            t2 = time.time()
            Mesh.stat_transform_time += (t1 - t0)
            Mesh.stat_render_time += (t2 - t1)

    # Implementation of object creation for the viewer
    @staticmethod
    def create_tetra(size, res_lat, res_lon, mesh=None):
        if mesh is None:
            mesh = Mesh("UnknownTetra")

        p0 = Vector3(0,0,0)
        p1 = Vector3(1,0,0)
        p2 = Vector3(0,1,0)
        p3 = Vector3(0,0,1)

        Mesh.create_tri(p0,p1,p2, mesh)
        Mesh.create_tri(p0,p2,p3, mesh)
        Mesh.create_tri(p0,p1,p3, mesh)

        return mesh
    
    @staticmethod
    def create_tri(p1, p2, p3, mesh):
        """
        Adds the vertices necessary to create a triangle
        If a source mesh is not given, a new mesh is created.
        Arguments:
            p1 {Vector3} -- First vertex of the triangle
            p2 {Vector3} -- Second vertex of the triangle
            p3 {Vector3} -- Third vertex of the triangle
            mesh {Mesh} -- Mesh to add the polygons. If not given, create a new mesh
        Returns:
            {Mesh} - Mesh where the polygons were added
        """
        if mesh is None:
            mesh = Mesh("UnknownQuad")

        poly = []
        poly.append(p1)
        poly.append(p2)
        poly.append(p3)

        mesh.polygons.append(poly)

        return mesh
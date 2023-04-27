# Winding order for Sentinel-3 geometry polygons

Sentinel-3 geometry polygons are a mix of:

- small chips, some of which cross the antimeridian
- large rectangles,
- complex, globe-spanning, pole-enclosing, self-overlapping, self-intersecting polygons.

Most Sentinel-3 polygons are CCW, but all or portions of some collections are incorrectly wound CW. Incorrect winding causes the [antimeridian](https://github.com/gadomski/antimeridian) package to produce bad results: garbage in, garbage out.

## What

This repo contains a heuristic approach to determining Sentinel-3 polygon winding.

- You shouldn't use it for any other purpose.

## Why

Shapely's `is_ccw` method is not reliable for the large complex polygons or the chips that cross the antimeridian. This repo provides a single method to handle the full variety of Sentinel-3 polygons.

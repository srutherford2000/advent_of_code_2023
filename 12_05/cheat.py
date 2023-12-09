#!/usr/bin/env python3
  
"""

Intervals and linear maps of intervals and composing linear maps into a single linear map?

Perhaps we can try to invert each linear map and propagate the endpoints of segments where
discontinuities happen since these are where minima and maxima occur.

Sufficient to find all induced interval end points after traversing all maps so that we only
need to test forward pass to location at these end points, which will include all discontinuities
and thus also the minima and maxima.

"invert" each map from location backwards to get induced interval end points.

given map
    s1  s1+l1-1   s2   s2+l2-1      s3  s3+l3-1
    d1  d1+l1-1   d2   d2+l2-1      d3  d3+l3-1
(where d_i, s_i are sorted in increasing order of d_i)

and interval end points in map output

  x1                 x2   x3           x4          x5
(also sorted in increasing order of x_i)

The induced interval end points for the map input
- map x_i to x_s_i in s_i domain
- sorted union of s_i and x_s_j

Potential optimization: remove endpoints that are not actual discontinuities for the output
of this particular map.

"""

from collections import defaultdict
import sys

in_file = open("input.txt")
lines = [l.strip() for l in in_file]
in_file.close()

orig_seeds = list(map(int, lines[0].split(': ')[1].split()))
seeds = orig_seeds[:]
for i in range(0, len(seeds), 2):
  seeds[i+1] = seeds[i] + seeds[i+1] - 1
seeds = sorted(seeds)
#print(seeds)

def parse_map(start):
  ln = start
  assert lines[ln].endswith('map:'), (lines[ln])
  ln += 1
  map_info = []
  while ln < len(lines) and lines[ln]:
    (d_start, s_start, rlen) = list(map(int, lines[ln].split()))
    map_info.append((d_start, s_start, rlen))
    ln += 1
  return ln + 1, map_info

ln, seed2soil = parse_map(2)
ln, soil2fert = parse_map(ln)
ln, fert2water = parse_map(ln)
ln, water2light = parse_map(ln)
ln, light2temp = parse_map(ln)
ln, temp2humid = parse_map(ln)
ln, humid2location = parse_map(ln)

def lookup_map(map_info, x):
  for (d_start, s_start, rlen) in map_info:
    if s_start <= x < s_start + rlen:
      return d_start + (x - s_start)
  return x

def seed2location(seed):
  soil = lookup_map(seed2soil, seed)
  fert = lookup_map(soil2fert, soil)
  water = lookup_map(fert2water, fert)
  light = lookup_map(water2light, water)
  temp = lookup_map(light2temp, light)
  humid = lookup_map(temp2humid, temp)
  location = lookup_map(humid2location, humid)
  return location

print('Part 1:')
print(min([seed2location(s) for s in orig_seeds]))

def inverse_lookup_map(map_info, y):
  for (d_start, s_start, rlen) in map_info:
    if d_start <= y < d_start + rlen:
      return s_start + (y - d_start)
  return y

def invert_map(map_info, output_endpts):
  if output_endpts:
    assert sorted(output_endpts) == output_endpts, output_endpts
    assert len(set(output_endpts)) == len(output_endpts), output_endpts
  map_endpts = [[(d_start, s_start), (d_start + rlen - 1, s_start + rlen - 1)] for (d_start, s_start, rlen) in map_info]
  map_endpts = [mpt for mpts in map_endpts for mpt in mpts]
  map_endpts.sort()

  output_src_endpts = sorted([inverse_lookup_map(map_info, y) for y in output_endpts])
  assert len(set(output_src_endpts)) == len(output_src_endpts), (output_src_endpts, output_endpts, map_info)
  input_src_endpts = sorted(set([x for (y, x) in map_endpts]))
  if input_src_endpts[0] > 0:
    input_src_endpts = [0, input_src_endpts[0] - 1] + input_src_endpts
  if input_src_endpts[-1] < sys.maxsize:
    input_src_endpts = input_src_endpts + [input_src_endpts[-1] + 1, sys.maxsize]
  input_endpts = sorted(set(output_src_endpts) | set(input_src_endpts))

  """
  print()
  print('inverting map', map_info)
  print('output_endpts', output_endpts)
  print('map_endpts', map_endpts)
  print('output_src_endpts', output_src_endpts)
  print('input_src_endpts', input_src_endpts)
  print('input_endpts', input_endpts)
  print()
  """

  return input_endpts

humid_endpts = invert_map(humid2location, [0, sys.maxsize])
temp_endpts = invert_map(temp2humid, humid_endpts)
light_endpts = invert_map(light2temp, temp_endpts)
water_endpts = invert_map(water2light, light_endpts)
fert_endpts = invert_map(fert2water, water_endpts)
soil_endpts = invert_map(soil2fert, fert_endpts)
seed_endpts = invert_map(seed2soil, soil_endpts)

def in_seed_range(seeds, s):
  return any([seeds[i] <= s <= seeds[i+1] for i in range(0, len(seeds), 2)])

# Intersect seed endpoints with seed ranges.
seed_endpts = [s for s in seed_endpts if in_seed_range(seeds, s)]
# Make sure to include the endpoints of the seed ranges.
seed_endpts = sorted(set(seed_endpts) | set(seeds))
#print(seed_endpts)
#print([(s, seed2location(s)) for s in seed_endpts])

print('Part 2:')
print(min([seed2location(s) for s in seed_endpts]))
# Day 5

### DISCLAIMER
My code for part 2, is to dang slow and cannot brute force due to the shear number of options. I was able to conceptually think of a better way which used back propogating the maps to get an original range ordered by what they return at the end. Couldn't write the code, I used the subreddit help page to find the solution that mirrored what I was conceptually understanding. That code is found in cheat.py. Solution from [link](https://topaz.github.io/paste/#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)

### --- Day 5: If You Give A Seed A Fertilizer ---
You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.

"A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.

"Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"

You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our food production problem. The latest Island Island Almanac just arrived and we're having trouble making sense of it."

The almanac (your [puzzle input](input.txt)) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

For example:
```
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
```
The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.

Consider again the example seed-to-soil map:
```
50 98 2
52 50 48
```
The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:
```
seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
```
With this map, you can look up the soil number required for each initial seed number:

Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.
The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
So, the lowest location number in this example is 35.

What is the lowest location number that corresponds to any of the initial seed numbers?

### --- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:
```
seeds: 79 14 55 13
```
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?
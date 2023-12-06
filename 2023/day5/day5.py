# ONLY FINISHED PART 1
# This was my attempt at solving part 2, didn't save part 1 code

import sys

class Range:

    def __init__(self, **kwargs) -> None:
        '''
        Create Range either from string or from int values
        '''
        if 'range_str' in kwargs:
            range_params = kwargs['range_str'].split()
            output, input, length = [int(x) for x in range_params]

            # lower is inclusive, upper is not
            self.offset = output - input
            self.lower = input
            self.upper = input + length
            
        elif 'lower' in kwargs and 'upper' in kwargs and 'offset' in kwargs:
            self.offset = kwargs['offset']
            self.lower = kwargs['lower']
            self.upper = kwargs['upper']
        
    
    def __repr__(self) -> str:
        return f'lower={self.lower} upper={self.upper} offset={self.offset}'
    
    def __eq__(self, __value: 'Range') -> bool:
        return self.lower == __value.lower and self.upper == __value.upper
    
    def intersection(self, range: 'Range') -> 'Range':
        '''
        Return overlapping range if exists
        '''
        # { self }
        #     | range |
        if self.lower < range.lower < self.upper < range.upper:
            return Range(lower=range.lower, upper=self.upper, offset=range.offset+self.offset)
        
        #      { self }
        # | range |
        if range.lower < self.lower < range.upper < self.upper:
            return Range(lower=self.lower, upper=range.upper, offset=range.offset+self.offset)
        
        #   { self }
        # |   range   |
        if range.lower < self.lower < self.upper < range.upper:
            return Range(lower=self.lower, upper=self.upper, offset=range.offset+self.offset)

        #   { range }
        # |    self    |
        if self.lower < range.lower < range.upper < self.upper:
            return Range(lower=range.lower, upper=range.upper, offset=range.offset+self.offset)
        
    def xor(self, range: 'Range') -> ['Range', 'Range']:
        '''
        Return symmetric difference of the 2 ranges (opposite of intersection)
        '''
        # { self }
        #     | range |
        if self.lower < range.lower < self.upper < range.upper:
            return [Range(lower=self.lower, upper=range.lower, offset=self.offset),
                    Range(lower=self.upper, upper=range.upper, offset=range.offset)]
        
        #      { self }
        # | range |
        if range.lower < self.lower < range.upper < self.upper:
            return [Range(lower=range.lower, upper=self.lower, offset=range.offset),
                    Range(lower=range.upper, upper=self.upper, offset=self.offset)]
        
        #   { self }
        # |   range   |
        if range.lower < self.lower < self.upper < range.upper:
            return [Range(lower=range.lower, upper=self.lower, offset=range.offset),
                    Range(lower=self.upper, upper=range.upper, offset=range.offset)]

        #   { range }
        # |    self    |
        if self.lower < range.lower < range.upper < self.upper:
            return [Range(lower=self.lower, upper=range.lower, offset=self.offset),
                    Range(lower=range.upper, upper=self.upper, offset=self.offset)]
        
    def union(self, range: 'Range') -> list['Range']:
        '''
        Return union of the 2 ranges
        If overlap, returns 3 ranges, with 3 different offsets
        If no overlap, return 2 ranges, with 2 different offsets
        If they are same, return 1 range, with 1 offset
        '''
        if range == self:
            return [Range(lower=self.lower, upper=self.upper, offset=self.offset+range.offset)]
        
        intersect = self.intersection(range)
        if intersect:
            return [intersect] + self.xor(range)
        return [self, range]
        

lines = [line.rstrip() for line in sys.stdin]

# seeds = list(map(int, lines.pop(0).replace('seeds: ', '').split()))
first_line = lines.pop(0).replace('seeds: ', '').split()
seed_pairs = [f'{first_line[i]} {first_line[i]} {first_line[i+1]}' for i in range(0, len(first_line), 2)]
seed_ranges = [Range(range_str=s) for s in seed_pairs]

print(seed_ranges)
lines.pop(0)

lb, ub = 768975, 1084205557




# r1 = Range(range_str='5 0 5')
# r2 = Range(range_str='5 2 5')
# r3 = Range(range_str='2 3 2')

# print(r1)
# print(r2)
# print(r3)
# print()

# print(r1.intersection(r2))
# print(r2.intersection(r1))
# print(r2.intersection(r3))
# print()

# print(r1.xor(r2))
# print(r2.xor(r1))
# print(r2.xor(r3))

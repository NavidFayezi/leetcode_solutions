class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        number_stations = len(gas)
        assert(number_stations == len(cost))
        start_gas = []
        
        # create a list of startup gas 
        for i in range(number_stations):
            start_gas.append(gas[i] - cost[i])
        
        # The algorithm below somehow resembles Kadanes algorithm.
        total_gas_left = 0
        current_buck = 0
        start = 0
        for i in range(number_stations):
            total_gas_left += start_gas[i]
            current_buck += start_gas[i]
            if current_buck < 0: 
                start = i + 1
                current_buck = 0

        if total_gas_left < 0:
            return -1
        return start
            
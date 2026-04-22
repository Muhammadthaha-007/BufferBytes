def chiefHopper(arr):
    for bot_energy in range(1,max(arr)+1):
        result = [bot_energy,]
        for height in arr:
            if height == bot_energy:
                result.append(bot_energy)
            else: 
                bot_energy += (bot_energy-height)
                result.append(bot_energy)
        found_negative = any(neg < 0 for neg in result)
        if not found_negative:
            return result[0]
            
print(chiefHopper([2,3,4,3,2]))
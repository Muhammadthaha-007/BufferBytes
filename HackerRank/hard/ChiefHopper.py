def chiefHopper(arr):
    for bot_energy in range(1,max(arr)+1):
        result = [bot_energy,]
        for height in arr:
            if height != bot_energy:
                bot_energy += (bot_energy-height)
            result.append(bot_energy)
        if not min(result) < 0:
            return result[0]

print(chiefHopper([2,3,4,3,2]))
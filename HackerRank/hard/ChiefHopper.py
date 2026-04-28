
def chiefHopper(arr):
    arr.reverse()
    energy = 0
    for height in arr:
        energy = (energy + height+1)//2
    return energy

print(chiefHopper([1,6,4]))






    # for bot_energy in range(1,max(arr)+1):
    #     result = [bot_energy]
    #     for height in arr:
    #         if height != bot_energy:
    #             bot_energy += (bot_energy-height)
    #         result.append(bot_energy)
    #     if not min(result) < 0:
    #         return result[0]
import math
def fare_calculator(distancekm):
  #base fare
  base_fare = 4.00
  
  fare_rate = 0.25/140

  distancem = distancekm * 1000

  #have to adjust distance travelled because not every distance is a multiple of 140
  adjustd = distancem/140 
  adjustd2 = 140 * math.floor(adjustd)
  
  #calculate total fare for distance traveled
  total_fare = base_fare + (adjustd2 * fare_rate)
  return total_fare
def main():
  #Ask user for distance they traveled
  distancekm = float(input("Enter the distance traveled in kilometers: "))
  
  #Calculate taxi fare for user
  fare = fare_calculator(distancekm)
  
  #Return fare to user
  print(f"The total fare for traveling {distancekm} kilometers is ${fare:.2f}")

if __name__ == "__main__":
  main()
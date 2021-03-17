def input_vel():
    ''' Esta función recibe pregunta al usuario por una velocidad lineal en [km/h] '''
    vel = float(input("Digite una velocidad lineal [km/h]: "))
    return vel

def conversion_vel(vel):
    vel_i=0.621371*vel
    return vel_i

def output_vel(vel_i):
    print("La velocidad lineal es:", format(vel_i,'.2f'), "mph")

def main():
    vel = input_vel()
    vel_conv = conversion_vel(vel)
    output_vel(vel_conv)
    
if __name__ == '__main__':
    main()

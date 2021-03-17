def fn_input_vel():
    ''' función que pregunta al usuario por una velocidad lineal (km/h) '''
    vel_kmph = float(input('Digite un valor de velocidad (km/h):'))
    return vel_kmph

def fn_conv_vel(vel):
    ''' función que convierte vel. SI a Sistema Inglés'''
    vel_mph = 0.621371 * vel
    return vel_mph

def fn_output_vel(vel):
    ''' función que presenta el resultado '''
    print('La velocidad es: ',format(vel,'.2f'),'mph')
    
def main_conv_vel():
    ''' programa principal '''
    vel = fn_input_vel()
    vel_conv = fn_conv_vel(vel)
    fn_output_vel(vel_conv)

if __name__ == '__main__':
    main_conv_vel()
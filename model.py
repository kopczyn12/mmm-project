import math

class Model:
    
    def __init__(self):
        
        #stale
        self.T = 20.
        self.P = 3.
        self.number_of_iterations = 5000 #ilosc iteracji
        self.h = self.T/self.number_of_iterations #dyskretny krok symulacji
        self.u = [0 for i in range(self.number_of_iterations)] #pobudzenie
        self.pulsation = 1/(self.T/self.P)* 2 * math.pi #pulsacja dla prostokatnego i sinusa
       
        

        #listy do "zbierania" danych
        self.t = [i*self.h for i in range(self.number_of_iterations)]
        self.place_euler = [0 for i in range(self.number_of_iterations)]
        self.x_euler = [0 for i in range(self.number_of_iterations)]
        self.v_euler = [0 for i in range(self.number_of_iterations)]
        self.x_rg4 = [0 for i in range(self.number_of_iterations)]
        self.v_rg4 = [0 for i in range(self.number_of_iterations)]
     
    #update zmiennych i pobudzenia
    def update_model(self, var_k1 = 1, var_k2 = 1, var_m = 1, var_b = 1, var_amp = 1, var_x_zero = 1, var_x_zero_higher = 1, pobudzenie = "sinus"):
        
        self.k1 = var_k1
        self.k2 = var_k2
        self.m = var_m
        self.b = var_b
        self.Amp = var_amp
        self.x_zero = var_x_zero
        self.x_zero_higher = var_x_zero_higher


        if pobudzenie == "sinus":

            for i in range(self.number_of_iterations):
                x = self.Amp * math.sin(self.pulsation*i *self.h)
                self.u[i] = x

        elif pobudzenie == "prostokat":

            for i in range(self.number_of_iterations):
                x = (self.Amp*math.sin(self.pulsation*i*self.h))
                if x > 0:
                    self.u[i] = self.Amp
                else:
                    self.u[i] = -self.Amp


        elif pobudzenie == "trojkatne":
            for i in range(self.number_of_iterations):
               x = self.Amp*math.asin(math.sin(self.pulsation*i*self.h))
               self.u[i] = x
        
        self.euler()
        self.rk4()


    #metoda eulera
    def euler(self):
        #warunki poczatkowe
        self.x_euler[0] = self.x_zero
        self.v_euler[0] = self.x_zero_higher
        for i in range(1, self.number_of_iterations):
            
            self.v_euler[i] = (self.v_euler[i-1] +(self.h*((self.k1+self.k2)*self.x_euler[i-1])/self.m +(self.u[i-1]-self.b*self.v_euler[i-1])/self.m))
            self.x_euler[i] = (self.x_euler[i-1] + self.h*self.v_euler[i-1])
            
            
    #metoda runge-kutty   
    def rk4(self):
        self.x_rg4[0] = self.x_zero
        self.v_rg4[0] = self.x_zero_higher
        for i in range(0, self.number_of_iterations):
            dx1 = self.h*self.v_rg4[i-1]
            dv1 = self.h*(((self.k1+self.k2)*self.x_rg4[i-1])/self.m +(self.u[i-1]-self.b*self.v_rg4[i-1])/self.m)

            dx2 = self.h*(self.v_rg4[i-1]+dv1/2)
            dv2 = (self.h+self.h/2)*(((self.k1+self.k2)*(self.x_rg4[i-1]+dx1/2))/self.m +(self.u[i-1]-self.b*(self.v_rg4[i-1]+dv1/2))/self.m)
            
            dx3 =self.h*(self.v_rg4[i-1]+dv2/2)
            dv3 =(self.h+self.h/2)*(((self.k1+self.k2)*(self.x_rg4[i-1]+dx2/2))/self.m +(self.u[i-1]-self.b*(self.v_rg4[i-1]+dv2/2))/self.m)

            dx4 = self.h*(self.v_rg4[i-1]+dv3)
            dv4 =(self.h+self.h)*(((self.k1+self.k2)*(self.x_rg4[i-1]+dx3))/self.m +(self.u[i-1]-self.b*(self.v_rg4[i-1]+dv3))/self.m)
            
            dx = (dx1 + 2*dx2 + 2*dx3 +dx4)/6
            dv = (dv1 + 2*dv2 + 2*dv3 +dv4)/6

            self.x_rg4[i] = self.x_rg4[i-1] + dx
            self.v_rg4[i] = self.v_rg4[i-1] + dv

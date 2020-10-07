# Tabla de amortización #

Primero llamaremos a la clase llamada amortizacon del archivo Amortizacion.py


```python
from Amortizacion import amortizacion 
```

Ahora imprimiremos la tabla de amortización 


```python
A=amortizacion(20000,25,10,'09/19/20','/Users/usuario/Desktop','Prueba')
A.Tabla()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Saldo inicial</th>
      <th>Pago</th>
      <th>Capital</th>
      <th>Interes</th>
      <th>Saldo final</th>
    </tr>
    <tr>
      <th>Fecha</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19/09/2020</th>
      <td>20000.00</td>
      <td>1067.43</td>
      <td>650.76</td>
      <td>416.67</td>
      <td>19349.24</td>
    </tr>
    <tr>
      <th>19/10/2020</th>
      <td>19349.24</td>
      <td>1067.43</td>
      <td>664.32</td>
      <td>403.11</td>
      <td>18684.92</td>
    </tr>
    <tr>
      <th>19/11/2020</th>
      <td>18684.92</td>
      <td>1067.43</td>
      <td>678.16</td>
      <td>389.27</td>
      <td>18006.76</td>
    </tr>
    <tr>
      <th>19/12/2020</th>
      <td>18006.76</td>
      <td>1067.43</td>
      <td>692.29</td>
      <td>375.14</td>
      <td>17314.47</td>
    </tr>
    <tr>
      <th>19/01/2021</th>
      <td>17314.47</td>
      <td>1067.43</td>
      <td>706.71</td>
      <td>360.72</td>
      <td>16607.76</td>
    </tr>
    <tr>
      <th>19/02/2021</th>
      <td>16607.76</td>
      <td>1067.43</td>
      <td>721.44</td>
      <td>345.99</td>
      <td>15886.32</td>
    </tr>
    <tr>
      <th>19/03/2021</th>
      <td>15886.32</td>
      <td>1067.43</td>
      <td>736.47</td>
      <td>330.96</td>
      <td>15149.85</td>
    </tr>
    <tr>
      <th>19/04/2021</th>
      <td>15149.85</td>
      <td>1067.43</td>
      <td>751.81</td>
      <td>315.62</td>
      <td>14398.04</td>
    </tr>
    <tr>
      <th>19/05/2021</th>
      <td>14398.04</td>
      <td>1067.43</td>
      <td>767.47</td>
      <td>299.96</td>
      <td>13630.57</td>
    </tr>
    <tr>
      <th>19/06/2021</th>
      <td>13630.57</td>
      <td>1067.43</td>
      <td>783.46</td>
      <td>283.97</td>
      <td>12847.11</td>
    </tr>
    <tr>
      <th>19/07/2021</th>
      <td>12847.11</td>
      <td>1067.43</td>
      <td>799.78</td>
      <td>267.65</td>
      <td>12047.33</td>
    </tr>
    <tr>
      <th>19/08/2021</th>
      <td>12047.33</td>
      <td>1067.43</td>
      <td>816.44</td>
      <td>250.99</td>
      <td>11230.89</td>
    </tr>
    <tr>
      <th>19/09/2021</th>
      <td>11230.89</td>
      <td>1067.43</td>
      <td>833.45</td>
      <td>233.98</td>
      <td>10397.44</td>
    </tr>
    <tr>
      <th>19/10/2021</th>
      <td>10397.44</td>
      <td>1067.43</td>
      <td>850.82</td>
      <td>216.61</td>
      <td>9546.62</td>
    </tr>
    <tr>
      <th>19/11/2021</th>
      <td>9546.62</td>
      <td>1067.43</td>
      <td>868.54</td>
      <td>198.89</td>
      <td>8678.08</td>
    </tr>
    <tr>
      <th>19/12/2021</th>
      <td>8678.08</td>
      <td>1067.43</td>
      <td>886.64</td>
      <td>180.79</td>
      <td>7791.44</td>
    </tr>
    <tr>
      <th>19/01/2022</th>
      <td>7791.44</td>
      <td>1067.43</td>
      <td>905.11</td>
      <td>162.32</td>
      <td>6886.33</td>
    </tr>
    <tr>
      <th>19/02/2022</th>
      <td>6886.33</td>
      <td>1067.43</td>
      <td>923.96</td>
      <td>143.47</td>
      <td>5962.37</td>
    </tr>
    <tr>
      <th>19/03/2022</th>
      <td>5962.37</td>
      <td>1067.43</td>
      <td>943.21</td>
      <td>124.22</td>
      <td>5019.16</td>
    </tr>
    <tr>
      <th>19/04/2022</th>
      <td>5019.16</td>
      <td>1067.43</td>
      <td>962.86</td>
      <td>104.57</td>
      <td>4056.30</td>
    </tr>
    <tr>
      <th>19/05/2022</th>
      <td>4056.30</td>
      <td>1067.43</td>
      <td>982.92</td>
      <td>84.51</td>
      <td>3073.38</td>
    </tr>
    <tr>
      <th>19/06/2022</th>
      <td>3073.38</td>
      <td>1067.43</td>
      <td>1003.40</td>
      <td>64.03</td>
      <td>2069.98</td>
    </tr>
    <tr>
      <th>19/07/2022</th>
      <td>2069.98</td>
      <td>1067.43</td>
      <td>1024.31</td>
      <td>43.12</td>
      <td>1045.67</td>
    </tr>
    <tr>
      <th>19/08/2022</th>
      <td>1045.67</td>
      <td>1067.43</td>
      <td>1045.65</td>
      <td>21.78</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>



Ahora veamos cuantos intereses pagados llevamos en el mes 5 


```python
A.Interes(5)
```

    Hasta la fecha 19/01/2021 has pagado $1944.910000 de intereses


Ahora veamos cuanto dinero llevamos pagado en el mes 7


```python
A.Pago(7)
```

    Hasta la fecha 19/03/2021 has pagado $7472.010000


Ahora hagamos una excel del archivo 



```python
A.Excel()
```


```python
from IPython.display import Image 
Image(filename='excel.jpg',width=10000,height=10000)
```




    
![jpeg](output_11_0.jpg)
    



package tempconversions;

class TemperatureConversionFormulae 
{
    public static double CelsiustoFahrenheit(double inputTemp)
    {
        double outputtemp= ((9.0/5.0) * inputTemp) + 32;//Celsius to Fahrenheit equation;
        return outputtemp;
    }
    public static double CelsiustoKelvin(double inputTemp)
    {
        double outputtemp= inputTemp + 273.15;//Celsius to Kelvin equation;
        return outputtemp;
    }
    public static double FahrenheittoCelsius(double inputTemp)
    {
        double outputtemp= (inputTemp-32)*(5.0/9.0);//Fahrenheit to Celsius equation;
        return outputtemp;
    }
    public static double FahrenheittoKelvin(double inputTemp)
    {
        double outputtemp= (inputTemp +459.67)*(5.0/9.0);//Fahrenheit to Celsius equation;;
        return outputtemp;
    }
    public static double kelvinToCelsius(double inputTemp)
    {
        double outputtemp= inputTemp -273.15;//Kelvin to Celsius equation;
        return outputtemp;
    }
    public static double KelvintoFahrenheit(double inputTemp)
    {
        double outputtemp= (inputTemp*(9.0/5.0))-459.67;//Kelvin to Fahrenheit;
        return outputtemp;
    }
} 

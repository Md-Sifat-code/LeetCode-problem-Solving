class Solution {
    public double[] convertTemperature(double celsius) {
        double kelvin = celsius + 273.15;
        double x = celsius *1.80 +32.00;
        double[] y = new double[2];

        y[0] = kelvin;
        y[1] = x;
        return y;
        
    }
}
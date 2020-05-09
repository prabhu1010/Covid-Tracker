<html>
<body>
<pre>
The purpose of this project was to get a sense of how much of an impact the Coronavirus will have over the countries of US, UK, Italy, Spain and Germany. So how exactly will this impact be measured? What parameters will help us grasp the situation as the cases keep on growing?

I felt that it would make sense to monitor the Daily New Cases in each country as ultimately the fatalities depend on this metric. Also if a country takes the right measures to stop infection from spreading, it will result in a fall of the daily new cases.

Since the infection cycle varies from country to country, it would be useful to look at the falling rate of a country that succeeeds in controlling the infection to an extent. Also, it is evident that the infection cycle goes through three phases:

1) Exponential growth towards the peak
2) Short duration at a peak while governments try to flatten the curve
3) Linear(as opposed to exponential) fall in cases due to increased social distancing.

Initially I was looking up the numbers on worldometer.info and copying them manually to a tracking spreadsheet on a daily basis. As time went on, I felt it was better to automate the process whereby:
1) A bash script pulls the data from worldometer.info and writes to a file
2) A python script reads the file, determines the peak, traces the numbers following the peak, and uses an Arithmetic Progression model to predict how many days are left until the Daily New Cases metric falls to 50 people a day.
</pre>
</body>
</html>

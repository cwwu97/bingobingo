import React, { PureComponent } from 'react';
import { BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import Typography from '@mui/material/Typography';
export default function Chart(chartData) {

  var numberData = [];
  for (let i = 1;i <= 80;i++) {
    numberData.push({"name":i.toString(), "freq": chartData['chartData']['num_freq'][i.toString()]});
  }

  const oddEvenTag = ['和','單','小','雙'];
  var oddEvenData = []
  for (let i = 0;i < oddEvenTag.length;i++) {
    oddEvenData.push({"name":oddEvenTag[i], "freq": chartData['chartData']['oddeven_freq'][oddEvenTag[i]]});
  }

  return (
    <>
      <div style={{ width: '100%', marginBottom: "30px", marginTop: "30px" }}>
        <Typography variant="h5" sx={{textAlign: "center", margin: "10px"}}>
          球號分佈  
        </Typography>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart width={150} height={40} data={numberData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" style={{fontSize: '1rem'}} angle={-90} interval={0} dx={-5} dy={10}  />
            <YAxis style={{fontSize: '1rem'}}/>
            <Tooltip />
            <Bar dataKey="freq">
              {numberData.map((entry, index) => (
                <Cell cursor="pointer" fill={'#82ca9d'} key={`cell-${index}`} />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
      <div style={{ width: '100%', marginBottom: "30px", marginTop: "30px" }}>
      <Typography variant="h5" sx={{textAlign: "center", margin: "10px"}}>
        單雙分佈  
      </Typography>
      <ResponsiveContainer width="100%" height={400}>
        <BarChart width={150} height={40} data={oddEvenData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" style={{fontSize: '1rem'}} angle={0} interval={0} dx={0} dy={10}  />
          <YAxis style={{fontSize: '1rem'}}/>
          <Tooltip />
          <Bar dataKey="freq">
            {oddEvenData.map((entry, index) => (
              <Cell cursor="pointer" fill={'#8884d8'} key={`cell-${index}`} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  </>
  );
}


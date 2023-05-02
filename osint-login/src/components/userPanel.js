import React, { useEffect, useState } from 'react';
import { Grid, Typography } from '@material-ui/core';
import GaugeChart from 'react-gauge-chart';

const UserPanel = () => {
  const [data,setData]=useState([]);
 useEffect(()=>{
  fetch("http://localhost:5000/hashes",{
    method:"POST",
    crossDomain: true,
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    body: JSON.stringify({
      email:"A@GMAIL.COM",
      date:"2023-05-02",
    }),
  })
  .then((res)=>res.json())
  .then((data)=>{
    console.log(data, "result");
    setData(data.data);
  });
 },[]);
  
  return (
    <div>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6} md={4}>
        <GaugeChart id="gauge-chart1" style={{width:300}}/>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Typography variant='h6'>Suspicious files:</Typography>
        <table style={{width:300}}>
        <tr>
         
          <th>Score</th>
          <th>identification</th>
          <th>sha256</th>
        </tr>
        {data.map((item, index) => (
              <tr key={index}>
              
                <td>{item.reputation}</td>
                <td>{item.malicious}</td>
                <td>{item.sha256}</td>
              </tr>
            ))}
       
        </table>
        </Grid>
      
        <Grid item xs={12} sm={6} md={4}>
        <Typography variant='h6'>Suspicious network connactions:</Typography>
        <table  style={{width:200}}>
        <tr>
          <th>Url</th>
          <th>identification</th>
        </tr>
        {data.map(i=>{
          return(
            <tr>
            <td>{i.MAC}</td>
            <td>{i.email}</td>
            <td>{i.user}</td>
            </tr>
          )
        })}
        </table>
        </Grid>
      </Grid>
    </div>
  );
};


export default UserPanel;


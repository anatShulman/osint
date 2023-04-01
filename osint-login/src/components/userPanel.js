import React from 'react';
import { Grid, Paper, Typography } from '@material-ui/core';
import GaugeChart from 'react-gauge-chart';

const UserPanel = () => {
  return (
    <div>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6} md={4}>
        <GaugeChart id="gauge-chart1" style={{width:'30%'}}/>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Paper>Item 2</Paper>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Paper>Item 3</Paper>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Paper>Item 4</Paper>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Paper>Item 5</Paper>
        </Grid>
      </Grid>
    </div>
  );
};


export default UserPanel;


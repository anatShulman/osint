import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import {
  AppBar,
  Button,
  Toolbar,
  Typography,
  makeStyles,
} from '@material-ui/core';




const AllMacines = () => {
  const [data,setData]=useState([]);
  useEffect(() => {
    fetch("http://localhost:5000/getMachines", {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data, "AllMachines");
        setData(data.data);
      });
  });

  // create a new array that contains only unique values
  const uniqueData = Array.from(new Set(data.map((item) => item.email))).map(
    (email) => {
      return data.find((item) => item.email === email);
    }
  );

  return (
    <div className="auth-wrapper">
      <div className="auth-inner" style={{ width: "auto" }}>
        <Typography variant="h4" gutterBottom>
          All Machines
        </Typography>
        <table style={{ width: 500 }}>
          <thead>
            <tr>
              <th>Email</th>
              <th>User</th>
              <th>MAC</th>
            </tr>
          </thead>
          <tbody>
            {uniqueData.map((item) => {
              return (
                <tr key={item._id}>
                  <td>{item.email}</td>
                  <td>{item.user}</td>
                  <td>{item.MAC}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default AllMacines;

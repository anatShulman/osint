import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import {
  AppBar,
  Button,
  Toolbar,
  Typography,
  makeStyles,
} from '@material-ui/core';



const SuspiciousResults = () => {
  const [data,setData]=useState([]);
  const [filesData, setFilesData] = useState([]);
  const [networkData, setNetworkData] = useState([]);

  useEffect(() => {

    fetch("http://localhost:5000/hashes", {
      method: "POST",
      crossDomain: true,
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
        "Access-Control-Allow-Origin": "*",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data, "result");
        setFilesData(data.data);
      });
  }, []);
  return (
    <div className="auth-wrapper">
    <div className="auth-inner" style={{width:"auto"}}>
      <Typography variant="h4" gutterBottom>
        Suspicious Results
    </Typography>
    <div style={{ margin: "2rem 0" }}>
        <Typography variant="h6">Suspicious files:</Typography>
        <table style={{ width: "100%" }}>
          <thead>
            <tr>
              <th>Instance</th>
              <th>Name</th>
              <th>Reputation</th>
              <th>Identification</th>
              <th>sha256</th>
              <th>Path</th>
            </tr>
          </thead>
          <tbody>
            {filesData.map((item, index) => (
              <tr key={index}>
                <td style={{ wordBreak: "break-word" }}>{item.instance}</td>
                <td style={{ wordBreak: "break-word" }}>{item.name}</td>
                <td style={{ wordBreak: "break-word" }}>{item.reputation}</td>
                <td style={{ wordBreak: "break-word" }}>{parseFloat(item.malicious).toFixed(2)}</td>
                <td style={{ wordBreak: "break-word" }}>{item.sha256}</td>
                <td style={{ wordBreak: "break-word" }}>{item.path}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div style={{ margin: "2rem 0" }}>
        <Typography variant="h6">Suspicious network connections:</Typography>
        <table style={{ width: "100%" }}>
          <thead>
            <tr>
              <th>Verdict</th>
              <th>URL / Connection</th>
            </tr>
          </thead>
          <tbody>
            {networkData.map((item, index) => (
              <tr key={index}>
                <td style={{ wordBreak: "break-word" }}>{item.verdict}</td>
                <td style={{ wordBreak: "break-word" }}>{item.url}</td>
              </tr>
        ))}
          </tbody>
        </table>
      </div>
    </div>
    </div>
  );
}
export default SuspiciousResults;

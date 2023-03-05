import React, { useState, useEffect } from "react";
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import FileDownloadIcon from '@mui/icons-material/FileDownload';
import { CSVLink } from 'react-csv';

export default function IconLabelButtons({ resdata }) {
  const [csvData, setCsvData] = useState([['Name', 'Description', 'Id', 'x_mitre_platforms', 'phase_name', 'x_mitre_detection']]);

  useEffect(() => {
    if (resdata.length) {
      const formatedData = resdata.map((item) => {
        return [item.name, item.path, item.description];
      });
    
      setCsvData((prevSetCsvData) => [prevSetCsvData[0], ...formatedData]);
    }
  }, [resdata]);

  useEffect(() => {
    console.log('resdata;', resdata.length)
    console.log('csvData;', csvData.length)
  }, [resdata, csvData]);
  
  return (
    <>{csvData.length === resdata.length + 1 && (<Stack direction="row" spacing={2}>
      <Button startIcon={<FileDownloadIcon />} variant="contained" style={{ right: "2%", top: "9%", position: "absolute" }}>
      <CSVLink data={resdata} filename='table' >Download Table</CSVLink>
      </Button>
    </Stack>)}</>
  );
}




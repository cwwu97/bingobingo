import React, { useMemo, useState } from "react";
import { Container, Row } from "react-bootstrap";
import Typography from '@mui/material/Typography';
// import { getTodayNumber } from "../apis/axios";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from "@mui/material";
import "../style.css"

const columns = ["期號","時間","球號","單雙"];

const BingoTable = ({ data }) => {
  // const [sortedKey, setSortedKey] = useState("")
  // const sortedNumber = useMemo(() => {
  //   if (!sortedKey) return data;
  //   const ordered = Object.keys(data).sort().reduce(
  //     (obj, sortedKey) => { 
  //       obj[sortedKey] = data[sortedKey]; 
  //       return obj;
  //     }, 
  //     {}
  //   );
  //   return data;
  // }, [data, sortedKey])
  const renderTableHeader = () => (
    <TableHead>
      <TableRow>
        {columns.map((column, index) => (
          <TableCell
            key={index}
            align="center"
            style={{ backgroundColor: "#90A4AE", color: "white" }}
          >
            {column}
          </TableCell>
        ))}
      </TableRow>
    </TableHead>
  );

  const renderTableBody = () => {
    return (
      <TableBody>
        {data.map((result, index) => (
          <TableRow hover tabIndex={-1} key={index}>
            <TableCell align="center">{result.id}</TableCell>
            <TableCell align="center">{result.date} {result.time}</TableCell>
            <TableCell align="center">
              <div className="circle"><p className="text">{result.num01}</p></div>
              <div className="circle"><p className="text">{result.num02}</p></div>
              <div className="circle"><p className="text">{result.num03}</p></div>
              <div className="circle"><p className="text">{result.num04}</p></div>
              <div className="circle"><p className="text">{result.num05}</p></div>
              <div className="circle"><p className="text">{result.num06}</p></div>
              <div className="circle"><p className="text">{result.num07}</p></div>
              <div className="circle"><p className="text">{result.num08}</p></div>
              <div className="circle"><p className="text">{result.num09}</p></div>
              <div className="circle"><p className="text">{result.num10}</p></div>
              <div className="circle"><p className="text">{result.num11}</p></div>
              <div className="circle"><p className="text">{result.num12}</p></div>
              <div className="circle"><p className="text">{result.num13}</p></div>
              <div className="circle"><p className="text">{result.num14}</p></div>
              <div className="circle"><p className="text">{result.num15}</p></div>
              <div className="circle"><p className="text">{result.num16}</p></div>
              <div className="circle"><p className="text">{result.num17}</p></div>
              <div className="circle"><p className="text">{result.num18}</p></div>
              <div className="circle"><p className="text">{result.num19}</p></div>
              <div className="circle"><p className="text">{result.num20}</p></div>
            </TableCell>
            <TableCell align="center">{result.odd_even}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    );
  };

  return (
    <Container style={{marginTop: "50px"}}>
        <Typography variant="h4" sx={{textAlign: "center", marginBottom: "20px"}}>
            今日開獎
        </Typography>
        <TableContainer>
            <Table sx={{ minWidth: 650 }} aria-label="variable table">
            {renderTableHeader()}
            {renderTableBody()}
            </Table>
        </TableContainer>
    </Container>
    
  );
};

export default BingoTable;
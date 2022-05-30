import { useState } from "react";
import Container from '@mui/material/Container';
import DatePicker from "react-datepicker";
import styled from 'styled-components';
import Button from "@mui/material/Button";
import { Row } from 'reactstrap';
import Chart from "./Components/Chart";
import BingoTable from "./Components/BingoTable";
import Input from "./Components/Input";
import CheckboxInput from "./Components/CheckboxInput";
import Header from "./Components/Header";
import { getTodayNumber } from "./apis/axios";
import { useQuery, useQueryClient } from "react-query";
import { getAnalysis } from "./apis/axios";
import './style.css';

function ExecutionPage() {
    const [currentPage, setCurrentPage] = useState("main");
    const query = useQuery("bingo", getTodayNumber);
    if (query.data === undefined) {
        return <div>Loading data...</div>;
    }

    const handleAnalysis = async (arg) => {
        console.log(arg);
        const chartData = await getAnalysis(arg);
        console.log(chartData);
    }
    
    return (
        <div>
            <Header setCurrentPage={setCurrentPage} />
            <Container>
                {currentPage === "main" && <BingoTable data={query.data} /> }
                {currentPage === "analysis" && <CheckboxInput handleAnalysis={handleAnalysis} />}
                {currentPage === "analysis" && <Chart />}
            </Container>
        </div>
    );
}

export default ExecutionPage


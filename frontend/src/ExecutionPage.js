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
    const [showChart, setShowChart] = useState(false);
    const [charts, setCharts] = useState();
    const query = useQuery("bingo", getTodayNumber);
    if (query.data === undefined) {
        return <div>Loading data...</div>;
    }

    const handleAnalysis = async (arg) => {
        const chartData = await getAnalysis(arg);
        setCharts(chartData[0]);
        setShowChart(true);
    }
    
    return (
        <div>
            <Header setCurrentPage={setCurrentPage} />
            <Container>
                {currentPage === "main" && <BingoTable data={query.data} /> }
                {currentPage === "analysis" && <CheckboxInput handleAnalysis={handleAnalysis} />}
                {currentPage === "analysis" && showChart === true && <Chart chartData={charts} />}
            </Container>
        </div>
    );
}

export default ExecutionPage


import { useState } from "react";
import Container from '@mui/material/Container';
import DatePicker from "react-datepicker";
import styled from 'styled-components';
import Button from "@mui/material/Button";
import { Row } from 'reactstrap';
import '../style.css';
import "react-datepicker/dist/react-datepicker.css";

const DatePickerWrapper = styled(({ className, ...props }) => (
    <DatePicker {...props} wrapperClassName={className} />
  ))`
    width: 100%;
  `;
  
  const Calendar = styled.div`
    border-radius: 10px;
    box-shadow: 0 6px 12px rgba(27, 37, 86, 0.16);
    overflow: hidden;
  `;
  
  const Popper = styled.div`
    position: absolute;
    top: 0;
    left: 0;
    z-index: 2;
  `;

function Input() {
    const [startDate, setStartDate] = useState(new Date());

    return (
        <div>
            <div style={{padding: "20px", display: "flex", margin: "auto"}}>
                請輸入日期：
                <DatePickerWrapper  
                    selected={startDate}
                    onChange={(date) => setStartDate(date)}
                    popperContainer={Popper}
                    calendarContainer={Calendar} 
                />
            </div>
            <div style={{margin: "20px", display: "flex"}}>
                請輸入期數：
                <input></input>
            </div>
            <Row style={{margin: "20px"}}>
                <div className="mt-3">
                    <Button className="me-3" variant="contained" >搜尋</Button>
                    <Button variant="contained" sx={{marginLeft: "20px"}}>查看圖表</Button>
                </div>
            </Row>
        </div>
    );
}

export default Input


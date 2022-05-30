import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Checkbox from '@mui/material/Checkbox';
import Typography from '@mui/material/Typography';
import FormControlLabel from '@mui/material/FormControlLabel';
import { Button } from "@mui/material"

const year = [2020,2021,2022];
const month = [1,2,3,4,5,6,7,8,9,10,11,12];
const day = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31];

export default function CheckboxInput({handleAnalysis}) {
    const [checked, setChecked] = useState([false, false, false]);
    const [checkMonth, setCheckMonth] = useState(JSON.parse(JSON.stringify(month)).fill(false));
    const [checkDay, setCheckDay] = useState(JSON.parse(JSON.stringify(day)).fill(false));

    const analysis = () => {
        let tmpY = [];
        let tmpM = [];
        let tmpD = [];
        for (let i = 0;i < checked.length;i++) {
            if (checked[i])
                tmpY.push(year[i]) 
        }
        for (let i = 0;i < checkMonth.length;i++) {
            if (checkMonth[i])
                tmpM.push(month[i]) 
        }
        for (let i = 0;i < checkDay.length;i++) {
            if (checkDay[i])
                tmpD.push(day[i]) 
        }
        handleAnalysis({"year":tmpY, "month":tmpM, "day":tmpD});
    }

    function allAreTrue(arr) {
        return arr.every(element => element === true);
    }

    function allAreFalse(arr) {
        return arr.every(element => element === false);
      }

    const handleChangeYearAll = (event) => {
        setChecked([event.target.checked, event.target.checked, event.target.checked]);
    };

    const handleChangeMonthAll = (event) => {
        setCheckMonth(JSON.parse(JSON.stringify(month)).fill(event.target.checked));
    };

    const handleChangeDayAll = (event) => {
        setCheckDay(JSON.parse(JSON.stringify(day)).fill(event.target.checked));
    };

    const handleChangeYear = (index) => {
        let tmp;
        if (checked[index] === true) 
            tmp = false
        else
            tmp = true
        let check = JSON.parse(JSON.stringify(checked));
        check[index] = tmp;
        setChecked([...check]);
    }

    const handleChangeMonth = (index) => {
        let tmp;
        if (checkMonth[index] === true) 
            tmp = false
        else
            tmp = true
        let check = JSON.parse(JSON.stringify(checkMonth));
        check[index] = tmp;
        setCheckMonth([...check]);
    }

    const handleChangeDay = (index) => {
        let tmp;
        if (checkDay[index] === true) 
            tmp = false
        else
            tmp = true
        let check = JSON.parse(JSON.stringify(checkDay));
        check[index] = tmp;
        setCheckDay([...check]);
    }

    const yearChildren = (
        <Box sx={{ display: 'flex', flexDirection: 'row', ml: 3 }}>
            {year.map((option,index) => {
                return (
                    <FormControlLabel
                        key={index}
                        label={option}
                        control={<Checkbox checked={checked[index]} onChange={()=>handleChangeYear(index)} />}
                    />)
            })}
        </Box>
    );

    const monthChildren = (
        <Box sx={{ display: 'flex', flexDirection: 'row', ml: 3 }}>
            {month.map((option,index) => {
                return (
                    <FormControlLabel
                        key={index}
                        label={option}
                        control={<Checkbox checked={checkMonth[index]} onChange={()=>handleChangeMonth(index)} />}
                    />)
            })}
        </Box>
    );

    const dayChildren = (
        <>
        <Box sx={{ display: 'flex', flexDirection: 'row', ml: 3 }}>
            {day.map((option,index) => {
                if (index < 17)
                    return (
                        <FormControlLabel
                            key={index}
                            label={option}
                            control={<Checkbox checked={checkDay[index]} onChange={()=>handleChangeDay(index)} />}
                        />)
            })}
        </Box>
        <Box sx={{ display: 'flex', flexDirection: 'row', ml: 3 }}>
        {day.map((option,index) => {
            if (index >= 17)
                return (
                    <FormControlLabel
                        key={index}
                        label={option}
                        control={<Checkbox checked={checkDay[index]} onChange={()=>handleChangeDay(index)} />}
                    />)
        })}
    </Box>
    </>
    );

  return (
    <div style={{border: "solid", padding: "20px", margin: "20px"}}>
        <Typography variant="h5" sx={{textAlign: "center"}}>
            請選擇開獎時間區段
        </Typography>
      <FormControlLabel
        label="Year"
        control={
          <Checkbox
            checked={allAreTrue(checked)}
            indeterminate={!(allAreTrue(checked)) && !(allAreFalse(checked))}
            onChange={handleChangeYearAll}
          />
        }
      />
      {yearChildren}
      <FormControlLabel
        label="Month"
        control={
          <Checkbox
            checked={allAreTrue(checkMonth)}
            indeterminate={!(allAreTrue(checkMonth)) && !(allAreFalse(checkMonth))}
            onChange={handleChangeMonthAll}
          />
        }
      />
      {monthChildren}
      <FormControlLabel
        label="Day"
        control={
          <Checkbox
            checked={allAreTrue(checkDay)}
            indeterminate={!(allAreTrue(checkDay)) && !(allAreFalse(checkDay))}
            onChange={handleChangeDayAll}
          />
        }
      />
      {dayChildren}
      <div style={{display: "flex", justifyContent: "center"}}>
        <Button variant="contained" onClick={analysis}>搜尋</Button>
      </div>
    </div>
  );
}

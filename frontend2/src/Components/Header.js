import React, { useState } from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Link from '@mui/material/Link';

const Header = ({setCurrentPage}) => {
  return (
    <AppBar position="static" style={{ background: '#808080' }}>
      <Toolbar>
        <Typography variant="h6" onClick={() => setCurrentPage("main")} sx = {{flexGrow: 1}} style={{hover: "cursor"}} color = "white">
          BingoBingo
        </Typography>
        <Button color="inherit" onClick={() => setCurrentPage("main")} sx = {{flexGrow: 0}}>
          首頁
        </Button>
        <Button color="inherit" onClick={() => setCurrentPage("analysis")} sx = {{flexGrow: 0}}>
          球號分析
        </Button>
        <Link href="https://www.taiwanlottery.com.tw/index_new.aspx" target="_blank" underline="none" sx={{color: "white"}}>
            <Button color="inherit" sx = {{flexGrow: 0}}>
                台彩官網
            </Button>
        </Link>
      </Toolbar>
    </AppBar>
  );
};

export default Header;

import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';

interface Props {
    name: string
    value: string
    icon: React.ElementType
}

export default function OverviewCard(props: Props) {
    return (
        <Card>
            <CardContent className='flex min-w-56'>
                <Box><props.icon className="h-14 w-14"/></Box>
                <Box>
                    <Typography variant="subtitle1" color="text.secondary" component="div">
                        {props.name}
                    </Typography>
                    <Typography component="div" variant="h5" className='text-center'>
                        {props.value}
                    </Typography>
                </Box>
            </CardContent>
        </Card>
    );
}

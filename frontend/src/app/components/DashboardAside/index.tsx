'use client';
import * as React from 'react';
import ListSubheader from '@mui/material/ListSubheader';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import HomeIcon from '@mui/icons-material/Home';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';
import { useRouter } from 'next/navigation'

interface RoutePaths {
  readonly [index: string]: string;
}

export default function DashboardAside() {
  const [currentPath, setCurrentPath] = React.useState<string>("overview");
  const router = useRouter()
  const paths = {
    "overview": "/dashboard",
    "customers": "/dashboard/customers",
    "costs": "/dashboard/costs"
  } as RoutePaths


  const handleListItemClick = (
    event: React.MouseEvent<HTMLDivElement, MouseEvent>,
    currentPath: string,
  ) => {
    setCurrentPath(currentPath);
    router.push(paths[currentPath])
  };

  return (
    <List
      component="nav"
      aria-labelledby="nested-list-subheader"
      subheader={
        <ListSubheader component="div" id="nested-list-subheader" className='bg-inherit'>
          Lucality: Dashboard
        </ListSubheader>
      }
    >
      <ListItemButton
        selected={currentPath === "overview"}
        onClick={(event) => handleListItemClick(event, "overview")}>
        <ListItemIcon>
          <HomeIcon />
        </ListItemIcon>
        <ListItemText primary="Overview" />
      </ListItemButton>
      <ListItemButton
        selected={currentPath === "customers"}
        onClick={(event) => handleListItemClick(event, "customers")}
      >
        <ListItemIcon>
          <AccountCircleIcon />
        </ListItemIcon>
        <ListItemText primary="Customers" />
      </ListItemButton>
      <ListItemButton
        selected={currentPath === "costs"}
        onClick={(event) => handleListItemClick(event, "costs")}
      >
        <ListItemIcon>
          <AttachMoneyIcon />
        </ListItemIcon>
        <ListItemText primary="Costs" />
      </ListItemButton>
    </List>
  );
}

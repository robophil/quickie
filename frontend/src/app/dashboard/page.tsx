import Stack from '@mui/material/Stack';
import OverviewCard from "../components/OverviewCard"
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import LeaderboardIcon from '@mui/icons-material/Leaderboard';

export default function DashboardHomePage() {
  return (
    <Stack direction="row" spacing={2}>
      <OverviewCard name='Costs' value='$500,000' icon={AttachMoneyIcon} />
      <OverviewCard name='Customers' value='56' icon={AccountCircleIcon} />
      <OverviewCard name='Active Campaigns' value='4' icon={LeaderboardIcon} />
    </Stack>
  )
}
import ExecutionPage from './ExecutionPage';
import { QueryClient, QueryClientProvider } from "react-query";
import './App.css';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ExecutionPage />
    </QueryClientProvider>
  );
}

export default App;

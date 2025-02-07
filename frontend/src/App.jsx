import React, { useState, useEffect } from 'react';
import { Container, Box, Paper, Typography, Alert } from '@mui/material';
import NewsGrid from './components/NewsGrid';
import DatePicker from './components/DatePicker';
import { fetchNews } from './services/api';

function App() {
  const [news, setNews] = useState([]);
  const [selectedDate, setSelectedDate] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadNews();
  }, [selectedDate]);

  const loadNews = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await fetchNews(selectedDate);
      setNews(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error('Error loading news:', error);
      setError("Impossible de charger les actualités. Veuillez réessayer plus tard.");
      setNews([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Actualités Crypto
      </Typography>
      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}
      <Box sx={{ display: 'flex', gap: 3, flexDirection: { xs: 'column', md: 'row' } }}>
        <Box sx={{ flex: 3 }}>
          <Paper sx={{ p: 2, mb: 2 }}>
            <NewsGrid news={news} loading={loading} />
          </Paper>
        </Box>
        <Box sx={{ flex: 1 }}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Filtrer par date
            </Typography>
            <DatePicker 
              value={selectedDate}
              onChange={(newDate) => {
                setSelectedDate(newDate);
                setNews([]);
              }}
            />
          </Paper>
        </Box>
      </Box>
    </Container>
  );
}

export default App; 
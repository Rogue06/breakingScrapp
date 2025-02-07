import React from 'react';
import { Grid, Skeleton, Typography } from '@mui/material';
import NewsCard from './NewsCard';

function NewsGrid({ news = [], loading }) {
  if (loading) {
    return (
      <Grid container spacing={2}>
        {[1, 2, 3].map((item) => (
          <Grid item xs={12} sm={6} md={4} key={item}>
            <Skeleton variant="rectangular" height={200} />
          </Grid>
        ))}
      </Grid>
    );
  }

  if (!Array.isArray(news) || news.length === 0) {
    return (
      <Typography variant="body1" color="text.secondary" align="center">
        Aucune actualité trouvée pour cette date.
      </Typography>
    );
  }

  return (
    <Grid container spacing={2}>
      {news.map((item, index) => (
        <Grid item xs={12} sm={6} md={4} key={index}>
          <NewsCard news={item} />
        </Grid>
      ))}
    </Grid>
  );
}

export default NewsGrid; 
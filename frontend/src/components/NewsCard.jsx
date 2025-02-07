import React from 'react';
import {
  Card,
  CardContent,
  CardMedia,
  Typography,
  CardActionArea,
  Box,
} from '@mui/material';
import { format } from 'date-fns';
import { fr } from 'date-fns/locale';

function NewsCard({ news }) {
  const formatDate = (dateString) => {
    try {
      const date = new Date(dateString);
      return format(date, 'dd MMMM yyyy', { locale: fr });
    } catch (e) {
      return dateString;
    }
  };

  return (
    <Card>
      <CardActionArea href={news.link} target="_blank" rel="noopener noreferrer">
        {news.image && (
          <CardMedia
            component="img"
            height="140"
            image={news.image}
            alt={news.title}
          />
        )}
        <CardContent>
          <Typography gutterBottom variant="h6" component="div">
            {news.title}
          </Typography>
          {news.content && (
            <Typography variant="body2" color="text.secondary" paragraph>
              {news.content}
            </Typography>
          )}
          <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mt: 1 }}>
            <Typography variant="body2" color="text.secondary">
              Source: {news.source}
            </Typography>
            <Typography variant="body2" color="text.secondary">
              {formatDate(news.date)}
            </Typography>
          </Box>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}

export default NewsCard; 
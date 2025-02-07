import React from 'react';
import { DatePicker as MuiDatePicker } from '@mui/x-date-pickers';
import { TextField } from '@mui/material';
import { format } from 'date-fns';

function DatePicker({ value, onChange }) {
  const handleDateChange = (newDate) => {
    if (newDate) {
      try {
        // S'assurer que la date est au bon format
        const formattedDate = new Date(format(newDate, 'yyyy-MM-dd'));
        onChange(formattedDate);
      } catch (error) {
        console.error('Erreur de format de date:', error);
      }
    } else {
      onChange(null);
    }
  };

  return (
    <MuiDatePicker
      label="Sélectionner une date"
      value={value}
      onChange={handleDateChange}
      slotProps={{ 
        textField: { 
          fullWidth: true,
          error: false 
        } 
      }}
      maxDate={new Date()}
      format="dd/MM/yyyy"
    />
  );
}

export default DatePicker; 
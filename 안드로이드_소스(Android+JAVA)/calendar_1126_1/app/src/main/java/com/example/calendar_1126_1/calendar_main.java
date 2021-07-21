package com.example.calendar_1126_1;

import android.content.Intent;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

public class calendar_main extends AppCompatActivity {
    CustomCalendarView customCalendarView;
    @Override
    protected  void onCreate (Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.calendar_main_layout);

        customCalendarView =(CustomCalendarView)findViewById(R.id.custom_calendar_view);
    }
}

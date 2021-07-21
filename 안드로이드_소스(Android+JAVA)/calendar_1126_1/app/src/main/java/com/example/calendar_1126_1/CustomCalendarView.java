package com.example.calendar_1126_1;

import android.app.AlertDialog;
import android.content.Context;
import android.os.Build;
import android.util.AttributeSet;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.GridView;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.TimePicker;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.lang.reflect.Array;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;
import java.util.Locale;

public class CustomCalendarView extends LinearLayout {
    ImageButton PreviousButton,NextButton;
    TextView CurrentDate;
    GridView gridView;
    private static final int MAX_CALENDAR_Days = 42;
    Calendar calendar = Calendar.getInstance(Locale.KOREA);
    Context context;
    SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy MMMM",Locale.KOREA);
    SimpleDateFormat monthFormat = new SimpleDateFormat("MMMM",Locale.KOREA);
    SimpleDateFormat yearFormat = new SimpleDateFormat("yyyy",Locale.KOREA);
    SimpleDateFormat eventDateFormate = new SimpleDateFormat("yyyy-MM-dd", Locale.KOREA);
    //temp1119
    SimpleDateFormat timeFormat = new SimpleDateFormat("K:mm a",Locale.KOREA);
    SimpleDateFormat dayFormat = new SimpleDateFormat("dd",Locale.KOREA);
    SimpleDateFormat my_monthFormat = new SimpleDateFormat("MM",Locale.KOREA);
    //temp1119

    MyGridAdapter myGridAdapter;
    AlertDialog alertDialog;
    List<Date> dates = new ArrayList<>();
    ArrayList<Events> eventsList = new ArrayList<>();

    //로그인된 아이디 확인
    final static MainActivity mainActivity = new MainActivity();
    String login_id = mainActivity.login_id;
    //로그인된 아이디 확인

    public CustomCalendarView(Context context) {
        super(context);
    }

    public CustomCalendarView(final Context context, @Nullable AttributeSet attrs) {
        super(context, attrs);
        this.context=context;
        IntializeLayout();//전체 틀 초기화
        SetupCalendar();//캘린더부분 초기화

        //이전달 보기
        PreviousButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                calendar.add(Calendar.MONTH,-1);
                SetupCalendar();
            }
        });

        //다음달 보기
        NextButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                calendar.add(Calendar.MONTH,1);
                SetupCalendar();
            }
        });

        //특정 일 짧은 클릭(추가기능)  ->버튼같은거 정리 필요
        gridView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, final int position, long id) {

                AlertDialog.Builder builder =new AlertDialog.Builder(context);
                builder.setCancelable(true);
                final View addView = LayoutInflater.from(parent.getContext()).inflate(R.layout.add_newevent_layout,null);
                EditText EventName = addView.findViewById(R.id.eventname);
                TimePicker timePicker = addView.findViewById(R.id.eventtime_byspin);
                EditText EventItem = addView.findViewById(R.id.eventitem);
                Button AddEvent = addView.findViewById(R.id.addevent);

                final String date = dayFormat.format(dates.get(position));
                final String month = my_monthFormat.format(dates.get(position));
                final String year = yearFormat.format(dates.get(position));

                builder.setView(addView);
                alertDialog = builder.create();
                alertDialog.show();

                AddEvent.setOnClickListener(new OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                            sche_add sche_add = new sche_add();
                            sche_add.insert_event(year,month,date,timePicker.getHour(),timePicker.getMinute(),EventName.getText().toString(), login_id,EventItem.getText().toString());
                        }
                        SetupCalendar();
                        alertDialog.dismiss();
                    }
                });
            }
        });

        gridView.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {
            @Override
            public boolean onItemLongClick(AdapterView<?> parent, View view, int position, long id) {
                AlertDialog.Builder builder = new AlertDialog.Builder(context);
                builder.setCancelable(true);
                View showView = LayoutInflater.from(parent.getContext()).inflate(R.layout.show_event_layout,null);
                RecyclerView recyclerView= showView.findViewById(R.id.EventsRV);
                RecyclerView.LayoutManager layoutManager = new LinearLayoutManager(showView.getContext());
                recyclerView.setLayoutManager(layoutManager);
                recyclerView.setHasFixedSize(true);

                String Date = dayFormat.format(dates.get(position));
                String month = my_monthFormat.format(dates.get(position));
                String year = yearFormat.format(dates.get(position));
                String php_date_format = year + "-" + month + "-" + Date;

                /*ArrayList<Events> eventsArrayList = new ArrayList<>();
                sche_view sche_view = new sche_view();
                sche_view.event_day_selectAll(eventsArrayList,php_date_format);
                ArrayList<Events> oneday_eventsArrayList = new ArrayList<>();
                for(int i = 0; i<eventsArrayList.size(); i++)
                {
                    if(login_id.equals(eventsArrayList.get(i).getID()))
                    {
                        Events temp_events = new Events();
                        temp_events.setDate(eventsArrayList.get(i).getDate());
                        temp_events.setEvent(eventsArrayList.get(i).getEvent());
                        temp_events.setItem(eventsArrayList.get(i).getItem());
                        oneday_eventsArrayList.add(temp_events);
                    }
                }*/
                //sche view system
                sche_view sche_view = new sche_view();
                //선택된 일자의 일정 조회
                ArrayList<Events> oneday_eventsArrayList = sche_view.view_choiced_oneday(php_date_format,login_id);

                EventRecyclerAdapter eventRecyclerAdapter = new EventRecyclerAdapter(showView.getContext() ,oneday_eventsArrayList);
                eventRecyclerAdapter.notifyDataSetChanged();
                recyclerView.setAdapter(eventRecyclerAdapter);
                builder.setView(showView);
                alertDialog=builder.create();
                if(oneday_eventsArrayList.size()>0) {
                    alertDialog.show();
                }
                else
                {
                    Toast.makeText(getContext(),"등록된 일정이 없습니다.",Toast.LENGTH_SHORT).show();
                }
                return true;
            }
        });
    }

    public CustomCalendarView(Context context, @Nullable AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    private void IntializeLayout(){
        LayoutInflater inflater = (LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        View view = inflater.inflate(R.layout.calendar_layout,this);
        NextButton = view.findViewById(R.id.nextBtn);
        PreviousButton = view.findViewById(R.id.previousBtn);
        CurrentDate = view.findViewById(R.id.current_Date);
        gridView = view.findViewById(R.id.gridview);
    }

    private void SetupCalendar(){
        String StartDate = dateFormat.format(calendar.getTime());
        CurrentDate.setText(StartDate);
        dates.clear();
        Calendar monthCalendar = (Calendar)calendar.clone();
        monthCalendar.set(Calendar.DAY_OF_MONTH,1);
        int FirstDayOfMonth = monthCalendar.get(Calendar.DAY_OF_WEEK)-1;
        monthCalendar.add(Calendar.DAY_OF_MONTH,-FirstDayOfMonth);

        ArrayList<Events> eventsArrayList = new ArrayList<>();
        sche_view sche_view = new sche_view();
        sche_view.event_view(eventsArrayList, login_id);

        while (dates.size() < MAX_CALENDAR_Days){
            dates.add(monthCalendar.getTime());
            monthCalendar.add(Calendar.DAY_OF_MONTH,1);
        }
        myGridAdapter = new MyGridAdapter(context,dates,calendar,eventsList);
        gridView.setAdapter(myGridAdapter);
    }

    private Date convertStringToDate(String dateInString){
        java.text.SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd", Locale.KOREA);
        Date date = null;
        try {
            date = format.parse(dateInString);
        } catch (java.text.ParseException e) {
            e.printStackTrace();
        }
        return date;
    }

}

package com.example.calendar_1126_1;

import android.app.Dialog;
import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class EventRecyclerAdapter extends RecyclerView.Adapter<EventRecyclerAdapter.MyViewHolder> {
    Context context;
    ArrayList<Events> arrayList;

    //로그인된 아이디 확인
    final static MainActivity mainActivity = new MainActivity();
    String login_id = mainActivity.login_id;
    //로그인된 아이디 확인

    public EventRecyclerAdapter(Context context, ArrayList<Events> arrayList) {
        this.context = context;
        this.arrayList = arrayList;
    }

    //리사이클러뷰에 들어갈 뷰 홀더를 할당하는 함수
    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.show_event_rowlayout,parent,false);

        return new MyViewHolder(view);
    }

    // 실제 각 뷰 홀더에 데이터를 연결해주는 함수,[ i는 0부터 - length까지로  순차적으로 들어옴]     ->여기에 modify 해줘야한다.
    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {
        Events events = arrayList.get(position);
        holder.event_value.setText(events.getEvent());
        holder.date_value.setText(events.getDate());
        holder.item_value.setText(events.getItem());
        //holder.Time.setText(events.getTime());  -> 반환형 찾아야함

        // 커스텀 다이얼로그를 정의하기위해 Dialog클래스를 생성한다.
        Dialog dlg = new Dialog(context);

        // 액티비티의 타이틀바를 숨긴다.
        dlg.requestWindowFeature(Window.FEATURE_NO_TITLE);

        // 커스텀 다이얼로그의 레이아웃을 설정한다.
        dlg.setContentView(R.layout.update_dialog);

        // 커스텀 다이얼로그를 노출한다.
        //dlg.show();

        // 커스텀 다이얼로그의 각 위젯들을 정의한다.
        EditText edit_date, edit_event, edit_item;
        edit_date = dlg.findViewById(R.id.dialog_edit_date);
        edit_event = dlg.findViewById(R.id.dialog_edit_event);
        edit_item = dlg.findViewById(R.id.dialog_edit_item);
        Button edit_Button = dlg.findViewById(R.id.edit_button);

        holder.date_value.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                //modify dialog
                edit_date.setText(events.getDate());
                edit_event.setText(events.getEvent());
                edit_item.setText(events.getItem());
                dlg.show();

                edit_Button.setOnClickListener(new View.OnClickListener(){
                    @Override
                    public void onClick(View v){
                        String str_edit_date = edit_date.getText().toString();
                        String edit_year = str_edit_date.substring(0,4);
                        String edit_month = str_edit_date.substring(5,7);
                        String edit_day = str_edit_date.substring(8,10);
                        String edit_time = str_edit_date.substring(11,19);

                        sche_modi sche_modi = new sche_modi();
                        String date_format_check = sche_modi.date_check(str_edit_date);

                        if(date_format_check.equals("OK") && edit_year.equals(events.getDate().substring(0,4)) && edit_month.equals(events.getDate().substring(5,7)) && edit_day.equals(events.getDate().substring(8,10))) {
                            sche_modi.update_event(login_id, events.getDate(), edit_month + "-" + edit_day + "-" + edit_year + "%20" + edit_time, edit_event.getText().toString(), edit_item.getText().toString());

                            arrayList.get(position).setDate(edit_date.getText().toString());
                            arrayList.get(position).setEvent(edit_event.getText().toString());
                            arrayList.get(position).setItem(edit_item.getText().toString());
                        }
                        else if(date_format_check.equals("OK") && (!edit_year.equals(events.getDate().substring(0,4)) || !edit_month.equals(events.getDate().substring(5,7)) || !edit_day.equals(events.getDate().substring(8,10)))){
                            sche_modi.update_event(login_id, events.getDate(), edit_month + "-" + edit_day + "-" + edit_year + "%20" + edit_time, edit_event.getText().toString(), edit_item.getText().toString());

                            arrayList.remove(position);
                        }
                        else
                        {
                            Toast.makeText(context, date_format_check,Toast.LENGTH_LONG).show();
                        }

                        notifyDataSetChanged();
                        dlg.dismiss();
                    }
                });
            }
        });
        holder.event_value.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                edit_date.setText(events.getDate());
                edit_event.setText(events.getEvent());
                edit_item.setText(events.getItem());
                dlg.show();

                edit_Button.setOnClickListener(new View.OnClickListener(){
                    @Override
                    public void onClick(View v){

                        String str_edit_date = edit_date.getText().toString();
                        String edit_year = str_edit_date.substring(0,4);
                        String edit_month = str_edit_date.substring(5,7);
                        String edit_day = str_edit_date.substring(8,10);
                        String edit_time = str_edit_date.substring(11,19);

                        sche_modi sche_modi = new sche_modi();
                        sche_modi.update_event(login_id,events.getDate(),edit_month+"-"+edit_day+"-"+edit_year+"%20"+edit_time,edit_event.getText().toString(),edit_item.getText().toString());


                        arrayList.get(position).setDate(edit_date.getText().toString());
                        arrayList.get(position).setEvent(edit_event.getText().toString());
                        arrayList.get(position).setItem(edit_item.getText().toString());

                        notifyDataSetChanged();
                        dlg.dismiss();
                    }
                });
            }
        });
        holder.item_value.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                edit_date.setText(events.getDate());
                edit_event.setText(events.getEvent());
                edit_item.setText(events.getItem());
                dlg.show();

                edit_Button.setOnClickListener(new View.OnClickListener(){
                    @Override
                    public void onClick(View v){

                        String str_edit_date = edit_date.getText().toString();
                        String edit_year = str_edit_date.substring(0,4);
                        String edit_month = str_edit_date.substring(5,7);
                        String edit_day = str_edit_date.substring(8,10);
                        String edit_time = str_edit_date.substring(11,19);

                        sche_modi sche_modi = new sche_modi();
                        sche_modi.update_event(login_id,events.getDate(),edit_month+"-"+edit_day+"-"+edit_year+"%20"+edit_time,edit_event.getText().toString(),edit_item.getText().toString());

                        notifyDataSetChanged();
                        arrayList.get(position).setDate(edit_date.getText().toString());
                        arrayList.get(position).setEvent(edit_event.getText().toString());
                        arrayList.get(position).setItem(edit_item.getText().toString());
                        dlg.dismiss();
                    }
                });
            }
        });


        //이벤트 삭제 이벤트
        holder.delete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //sche del system
                sche_del sche_del = new sche_del();
                //일정 삭제
                sche_del.delete_event(login_id,events.getDate().substring(0,10)+"%20"+events.getDate().substring(11,19));
                arrayList.remove(position);     //view 목록에서 삭제
                notifyDataSetChanged();         //새로고침
            }
        });

    }

    //리사이클러뷰안에 들어갈 뷰 홀더의 개수
    @Override
    public int getItemCount() {
        return arrayList.size();
    }

    public class MyViewHolder extends RecyclerView.ViewHolder{
        //조회관련
        TextView date, date_value, event, event_value, item, item_value;
        Button delete;

        //각 뷰에 들어갈 아이템 지정
        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            date = itemView.findViewById(R.id.text_date);
            date_value = itemView.findViewById(R.id.data_date);
            event = itemView.findViewById(R.id.text_event);
            event_value = itemView.findViewById(R.id.data_event);
            item = itemView.findViewById(R.id.text_item);
            item_value = itemView.findViewById(R.id.data_item);
            delete = itemView.findViewById(R.id.delete);
        }
    }
}

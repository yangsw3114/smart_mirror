package com.example.calendar_1126_1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    public static ArrayList<Users> user_list = new ArrayList<>();
    public static String login_id = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button login_button = findViewById(R.id.Login);
        Button register_button = findViewById(R.id.btn_register);
        EditText editText_id = findViewById(R.id.ID);
        EditText editText_pw = findViewById(R.id.pass_ward);

        dbGet dbget = new dbGet();
        dbget.user_selectAll(user_list);

        login_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent_calendar = new Intent(getApplicationContext(), calendar_main.class);

                //Login system 클래스
                login_check login_check = new login_check();
                //Login system check_login함수 호출
                String check_id_pw = login_check.check_login(editText_id.getText().toString(),editText_pw.getText().toString(),user_list);

                //Login system의 결과에 따라 이벤트 처리
                if (check_id_pw.equals("OK"))
                {
                    login_id = editText_id.getText().toString();
                    startActivity(intent_calendar);
                }
                else if (check_id_pw.equals("PW_check"))
                {
                    Toast.makeText(getApplicationContext(), "비밀번호가 틀립니다.", Toast.LENGTH_LONG).show();
                }
                else if (check_id_pw.equals("ID_None"))
                {
                    Toast.makeText(getApplicationContext(), "존재하지 않는 아이디입니다.", Toast.LENGTH_LONG).show();
                }
                else
                {
                    Toast.makeText(getApplicationContext(), "로그인 에러", Toast.LENGTH_LONG).show();
                }
            }
        });

        register_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent_register = new Intent(getApplicationContext(), register_main.class);
                startActivity(intent_register);
            }
        });
    }
}
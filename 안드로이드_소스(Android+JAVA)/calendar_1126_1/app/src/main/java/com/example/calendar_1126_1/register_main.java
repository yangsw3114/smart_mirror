package com.example.calendar_1126_1;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;
import java.util.List;

public class register_main extends AppCompatActivity {
    private EditText edittext_id, edittext_password, edittext_name, edittext_tel;
    private Button j_button, check_button, back_button,camera_button;

    final static MainActivity mainActivity = new MainActivity();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register_main);

        user_join user_join = new user_join();

        //아이디값 찾아주기
        edittext_id = findViewById(R.id.join_id);
        edittext_password = findViewById( R.id.join_password );
        edittext_name = findViewById( R.id.join_name );
        edittext_tel = findViewById(R.id.join_tel);

        final boolean[] id_check_flag = {false};


        //아이디 중복 체크
        check_button = findViewById(R.id.check_id_button);
        check_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(user_join.check_id_overlap(edittext_id.getText().toString()))
                {
                    Toast.makeText(getApplicationContext(),"사용 가능한 아이디 입니다.",Toast.LENGTH_SHORT).show();
                    id_check_flag[0] = true;
                }
                else {
                    Toast.makeText(getApplicationContext(), "이미 존재하는 아이디입니다.", Toast.LENGTH_SHORT).show();
                    edittext_id.setText("");
                }
            }
        });


        //회원가입
        j_button = findViewById( R.id.join_button);
        j_button.setOnClickListener( new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int tel_size = edittext_tel.getText().toString().length();
                boolean tel_size_flag = false;
                if(tel_size==11)
                {
                    tel_size_flag=true;
                }


                if(id_check_flag[0] == true && tel_size_flag==true) {
                    user_join.join_user(edittext_id.getText().toString(), edittext_password.getText().toString(), edittext_name.getText().toString(), edittext_tel.getText().toString());
                    Toast.makeText(getApplicationContext(),"회원가입 성공!",Toast.LENGTH_SHORT).show();
                    onBackPressed();
                }
                else if(id_check_flag[0] ==false)
                {
                    Toast.makeText(getApplicationContext(),"아이디 중복을 확인해주세요.",Toast.LENGTH_SHORT).show();
                }
                else if(tel_size_flag==false)
                {
                    Toast.makeText(getApplicationContext(),"전화번호를 올바르게 입력해주세요.",Toast.LENGTH_SHORT).show();
                }
                else{
                    Toast.makeText(getApplicationContext(),"회원가입 요건이 충족되지 않았습니다.",Toast.LENGTH_SHORT).show();
                }

                /*dbGet dbget = new dbGet();

                List<String> join_data = new ArrayList<>();

                ArrayList<Users> to_add_user_list = mainActivity.user_list;

                Users to_add_users = new Users();

                to_add_users.setID(edittext_id.getText().toString());
                to_add_users.setPW(edittext_password.getText().toString());
                to_add_users.setNAME(edittext_name.getText().toString());
                to_add_users.setTEL(edittext_tel.getText().toString());
                to_add_user_list.add(to_add_users);


                join_data.add(edittext_id.getText().toString());
                join_data.add(edittext_password.getText().toString());
                join_data.add(edittext_name.getText().toString());
                join_data.add(edittext_tel.getText().toString());

                dbget.insert("MIRRORUSER", join_data);

                Toast.makeText(getApplicationContext(),"join_success!!!",Toast.LENGTH_SHORT).show();
                onBackPressed();*/
            }
        });


        //메인메뉴로
        back_button = findViewById(R.id.backtomain_button);
        back_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(),"cancle",Toast.LENGTH_SHORT).show();
                onBackPressed();
            }
        });

        /*camera_button = findViewById(R.id.camera_button);
        camera_button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Toast.makeText(getApplicationContext(),"camera",Toast.LENGTH_SHORT).show();

                Intent intent_camera = new Intent(getApplicationContext(), camera_main.class);
                startActivity(intent_camera);
            }
        });*/
    }
}

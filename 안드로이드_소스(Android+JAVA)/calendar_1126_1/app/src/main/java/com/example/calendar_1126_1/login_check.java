package com.example.calendar_1126_1;

import java.util.ArrayList;

public class login_check {

    public String check_login(String id, String pw,ArrayList<Users> users)
    {
        String return_string = null;
        for (int i = 0; i < users.size(); i++) {
            //아이디 비밀번호 모두 일치하는 경우
            if (id.equals(users.get(i).getID()) && pw.equals(users.get(i).getPW()))
            {
                return_string = "OK";
                break;
            }
            //아이디만 일치하는 경우
            else if (id.equals(users.get(i).getID()) && !pw.equals(users.get(i).getPW())) {
                return_string = "PW_check";
                break;
            }
            //입력된 아이디가 없는 아이디인 경우
            else if (!id.equals(users.get(i).getID())) {
                return_string = "ID_None";
            }
        }
        return return_string;
    }
}

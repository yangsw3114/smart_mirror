package com.example.calendar_1126_1;

import android.util.Log;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;

public class sche_modi {
    public String link = "http://doran2322.iptime.org:8080/db.php?FLAG=";
    public String tablename;
    public List<String> data;
    public String filter;
    public String result;

    public void update(String tablename, String filter1, String filter_data1,String filter2,String filter_data2,String u_filter1,String u_data1,String u_filter2,String u_data2,String u_filter3,String u_data3) {
        String filter_data2_1 = filter_data2.substring(0,10);
        String filter_data2_2 = filter_data2.substring(11,19);

        this.tablename = tablename;

        this.link += "UPDATE" + "&TABLENAME=" + tablename + "&ROW0=" + filter1 + "&ROW1=" + filter_data1 + "&ROW2=" + filter2 + "&ROW3=" + filter_data2_1+"%20"+filter_data2_2 + "&ROW4=" + u_filter1 + "&ROW5=" + u_data1 + "&ROW6=" + u_filter2 + "&ROW7=" + u_data2 + "&ROW8=" + u_filter3 + "&ROW9=" + u_data3;
        Log.v("insert_check",link);
        new Thread() {
            @Override
            public void run() {
                try {
                    URL url = new URL(link);
                    HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                    connection.setRequestMethod("GET"); //전송방식
                    connection.setDoOutput(true);       //데이터를 쓸 지 설정
                    connection.setDoInput(true);        //데이터를 읽어올지 설정

                    InputStream is = connection.getInputStream();
                    StringBuilder sb = new StringBuilder();
                    BufferedReader br = new BufferedReader(new InputStreamReader(is, "UTF-8"));
                    while ((result = br.readLine()) != null) {
                        sb.append(result + "\n");
                    }
                    result = sb.toString();

                } catch (MalformedURLException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();
    }

    public void  update_event(String id, String filter_time, String u_time, String u_event, String u_item)
    {
        update("DETAILDAY","ID","b","TIME",filter_time,"TIME",u_time ,"PLAN",u_event,"ITEM",u_item);
    }

    public String date_check(String date)
    {
        int monthArr[] = {31,28,31,30,31,30,31,31,30,31,30,31,0};

        String year = date.substring(0,4);
        String month = date.substring(5,7);
        String day = date.substring(8,10);
        String hour = date.substring(11,13);
        String minute = date.substring(14,16);
        String second = date.substring(17,19);

        String first_ = date.substring(4,5);
        String second_ = date.substring(7,8);
        String blank = date.substring(10,11);
        String first_thang = date.substring(13,14);
        String second_thang = date.substring(16,17);

        int int_year = Integer.parseInt(date.substring(0,4));
        int int_month = Integer.parseInt(date.substring(5,7));
        int int_day = Integer.parseInt(date.substring(8,10));
        int int_hour = Integer.parseInt(date.substring(11,13));
        int int_minute = Integer.parseInt(date.substring(14,16));
        int int_second = Integer.parseInt(date.substring(17,19));

        if(((int_year%4 == 0) && (int_year % 100 != 0) ) || (int_year % 400 == 0))
        {
            monthArr[1] = 28; //윤년
            int compare_m_value = monthArr[int_month-1];

            //해당 월에맞게 일자를 입력 안한경우
            if(int_day>compare_m_value)
            {
                return "해당 월의 최대값보다 입력월 값이 큽니다.";
            }
            if(int_day<0)
            {
                return "월을 0이하로 입력할 수 없습니다.";
            }

            //1900년대 이하인경우
            if(int_year<1900)
            {
                return "너무 과거입니다. (1900년 미만)";
            }
            //2100년 이상인경우
            if(int_year>2100)
            {
                return "너무 미래입니다. (2100년 초과)";
            }
            //월을 1~12사이로 입력하지 않은경우
            if(int_month<1 || int_month >12)
            {
                return "월을 1~12사이로 입력해주세요.";
            }
            //시간을 범위에 맞지않게 입력한경우
            if(int_hour <0 || int_hour>24)
            {
                return "시간을 0~24사이로 입력해주세요.";
            }
            //분을 범위에 맞지않게 입력한경우
            if(int_minute <0 || int_minute>60)
            {
                return "분을 0~60 사이로 입력해주세요.";
            }
            //초를 범위에 맞지않게 입력한경우
            if(int_second<0 || int_second>60)
            {
                return "초를 0~60 사이로 입력해주세요.";
            }
            //년월일 사이를 -로입력안한경우
            if(!first_.equals("-") || !second_.equals("-"))
            {
                return "년,월,일 사이의 -을 확인하세요.";
            }
            //일자와 시간 사이를 ' '으로 입력안한경우
            if(!blank.equals(" "))
            {
                return "일자와 시간 사이에 공백으로 넣어주세요.";
            }
            //시,분,초 사이를 : 로 입력안한경우
            if(!first_thang.equals(":") || !second_thang.equals(":"))
            {
                return "시,분,초 사이의 :를 확인하세요";
            }
            if(date.length()!=19)
            {
                return "time의 형식을 잘못 입력하셨습니다.";
            }
            return "OK";
        }
        else
        {
            monthArr[1] = 29; //윤년이 아닐 때
            int compare_m_value = monthArr[int_month-1];
            //윤년아님

            //해당 월에맞게 일자를 입력 안한경우
            if(int_day>compare_m_value)
            {
                return "해당 월의 최대값보다 입력월 값이 큽니다.";
            }
            else if(int_day<0)
            {
                return "월을 0이하로 입력할 수 없습니다.";
            }

            //1900년대 이하인경우
            if(int_year<1900)
            {
                return "너무 과거입니다. (1900년 미만)";
            }
            //2100년 이상인경우
            if(int_year>2100)
            {
                return "너무 미래입니다. (2100년 초과)";
            }
            //월을 1~12사이로 입력하지 않은경우
            if(int_month<1 || int_month >12)
            {
                return "월을 1~12사이로 입력해주세요.";
            }
            //시간을 범위에 맞지않게 입력한경우
            if(int_hour <0 || int_hour>24)
            {
                return "시간을 0~24사이로 입력해주세요.";
            }
            //분을 범위에 맞지않게 입력한경우
            if(int_minute <0 || int_minute>60)
            {
                return "분을 0~60 사이로 입력해주세요.";
            }
            //초를 범위에 맞지않게 입력한경우
            if(int_second<0 || int_second>60)
            {
                return "초를 0~60 사이로 입력해주세요.";
            }
            //년월일 사이를 -로입력안한경우
            if(!first_.equals("-") || !second_.equals("-"))
            {
                return "년,월,일 사이의 -을 확인하세요.";
            }
            //일자와 시간 사이를 ' '으로 입력안한경우
            if(!blank.equals(" "))
            {
                return "일자와 시간 사이에 공백으로 넣어주세요.";
            }
            //시,분,초 사이를 : 로 입력안한경우
            if(!first_thang.equals(":") || !second_thang.equals(":"))
            {
                return "시,분,초 사이의 :를 확인하세요";
            }
            if(date.length()!=19)
            {
                return "time의 형식을 잘못 입력하셨습니다.";
            }

            return "OK";
        }
    }

}

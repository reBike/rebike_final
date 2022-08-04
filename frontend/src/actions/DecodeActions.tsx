import { Dispatch } from "redux";
import jwtDecode from "jwt-decode";
import {
  DecodeDispatchType,
  DecodePropsType,
  DECODE_SUCCESS,
  DECODE_FAIL,
} from "./DecodeActionTypes";

interface jwtType {
  alias: string;
  exp: string;
  id: string;
  type: string;
}

export const fetchDecodeData =
  (accessToken: string) => (dispatch: Dispatch<DecodeDispatchType>) => {
    if (accessToken) {
      const decoded = jwtDecode<jwtType>(accessToken); // Returns with the JwtPayload type

      const data: DecodePropsType = {
        id: decoded.id, //반환된 데이터의 Email 값 사용
        alias: decoded.alias,
      };

      dispatch({
        type: DECODE_SUCCESS,
        payload: data,
      });
    } else {
      dispatch({
        type: DECODE_FAIL,
      });
    }
  };

//dispatch로 호출해서 토큰을 받아오도록

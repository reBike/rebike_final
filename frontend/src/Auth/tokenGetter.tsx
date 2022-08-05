import jwtDecode, { JwtPayload } from "jwt-decode";

// 해더에 사용할 닉네임을 위해 받아온 token 디코드
const decodeToken = (accessToken: string) => {

  if (process.env.REACT_APP_SECRET_KEY && process.env.REACT_APP_ALGORITHM) {
    const decoded = jwtDecode<JwtPayload>(accessToken); // Returns with the JwtPayload type


    return decoded;
  }
};

export { decodeToken };

import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 10 },
    { duration: '1m', target: 10 },
    { duration: '30s', target: 0 },
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
    login_duration: ['p(95)<1000'],
  },
};

export function setup() {
  const loginPayload = {
    email: 'hnoihnoi50@gmail.com', 
    password: '123456', 
    returnSecureToken: true,
  };

  const loginRes = http.post(
    'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyCBBOwar3xoFDUfGQYSd3r6zMGvr23h6fQ',
    JSON.stringify(loginPayload),
    { headers: { 'Content-Type': 'application/json' } }
  );

  check(loginRes, { 'login successful': (r) => r.status === 200 });
  return { token: loginRes.json('idToken') };
}

export default function (data) {
  const headers = {
    'Authorization': `Bearer ${data.token}`,
    'Content-Type': 'application/json',
  };

  const res = http.get('https://api-v2.xno.vn/reports/v1/reports?page=0&limit=15', { headers });

  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });

  sleep(1);
}
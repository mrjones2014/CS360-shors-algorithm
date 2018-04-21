OPENQASM 2.0;
include "qelib1.inc";

qreg q[4];
creg ans[4];


x q[0];
x q[1];
x q[3];
x q[0];
x q[1];
x q[2];
x q[3];
cx q[2], q[1];
cx q[1], q[2];
cx q[2], q[1];
cx q[1], q[0];
cx q[0], q[1];
cx q[1], q[0];
cx q[3], q[0];
cx q[0], q[3];
cx q[3], q[0];
measure q[0] -> ans[0];
measure q[1] -> ans[1];
measure q[2] -> ans[2];
measure q[3] -> ans[3];
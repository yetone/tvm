# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# pylint: disable=missing-docstring
import tvm
from tvm import tir


def test_tir_op_tvm_tuple():
    x = tir.Var("x", dtype="float32")
    y = tir.Var("y", dtype="float32")
    z = tir.Var("z", dtype="float32")
    expr = tir.tvm_tuple(x, y, z, 1, 2, 3)
    assert expr.op.name == "tir.tvm_tuple"


def test_tir_op_tvm_struct_get():
    x = tir.Var("x", dtype="handle")
    expr = tir.tvm_struct_get(x, 1, 2, dtype="int32")
    assert expr.op.name == "tir.tvm_struct_get"


def test_tir_op_tvm_struct_set():
    x = tir.Var("x", dtype="handle")
    expr = tir.tvm_struct_set(x, 1, 2, 3)
    assert expr.op.name == "tir.tvm_struct_set"


def test_tir_op_call_assume():
    x = tir.Var("x", dtype="int32")
    expr = tir.assume(cond=x)
    assert expr.op.name == "tir.assume"


def test_tir_op_call_undef():
    expr = tir.undef()
    assert expr.op.name == "tir.undef"


def test_tir_op_call_likely():
    x = tir.Var("x", dtype="int32")
    expr = tir.likely(cond=x)
    assert expr.op.name == "tir.likely"


if __name__ == "__main__":
    test_tir_op_tvm_tuple()
    test_tir_op_tvm_struct_get()
    test_tir_op_tvm_struct_set()
    test_tir_op_call_assume()
    test_tir_op_call_undef()
    test_tir_op_call_likely()

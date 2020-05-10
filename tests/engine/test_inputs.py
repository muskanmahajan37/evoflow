# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from geneflow.ops import Input
from geneflow import backend as B


def test_1d():
    shape = (128, 64)
    population = B.randint(1, 10, shape=shape)
    inputs = Input(shape)
    inputs.assign(population)
    assert inputs.call(population).all() == population.all()


def test_2d():
    shape = (128, 64, 64)
    population = B.randint(1, 10, shape=shape)
    inputs = Input(shape)
    inputs.assign(population)
    assert inputs.call(population).all() == population.all()
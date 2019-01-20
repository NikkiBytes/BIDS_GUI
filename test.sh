#!/bin/bash

id="sub-001"
echo $id
input=$1
cmd=${input//SUBJECT/$id}
echo $cmd

from json2csv_api.models import Json, Csv

class TestJson:
    def test_json(self) -> None:
        obj_one = Json(a=1, b=2)
        obj_two = Json(**{'a': 1, 'b': 2})
        assert 1 == obj_one['a']
        assert 2 == obj_one['b']
        assert 1 == obj_two['a']
        assert 2 == obj_two['b']

    def test_parse(self) -> None:
        valid = "{\"a\": 1, \"b\": [1, 2]}"
        invalid = "{\"a\": 1, b: 2"
        obj = Json.parse(valid)
        assert 1 == obj['a']
        assert [1, 2] == obj['b']
        try:
            Json.parse(invalid)
            assert False
        except Exception:
            assert True

    def test_validate(self) -> None:
        valid = Json(**{
            "student1": ["view_grades", "view_classes"],
            "student2": ["view_grades", "view_classes"],
            "teacher": ["view_grades", "change_grades", "add_grades", "delete_grades", "view_classes"]
        })
        invalid = Json(**{"records": [
            {"student1": ["view_grades", "view_classes"]},
            {"student2": ["view_grades", "view_classes"]},
            {"teacher": ["view_grades", "change_grades", "add_grades", "delete_grades", "view_classes"]}
        ]})
        assert valid.validate()
        assert not invalid.validate()

    def test_iter(self) -> None:
        it = iter(Json(**{
            "student1": ["view_grades", "view_classes"],
            "student2": ["view_grades", "view_classes"],
            "teacher": ["view_grades", "change_grades", "add_grades", "delete_grades", "view_classes"]
        }))
        iter_one = next(it)
        next(it)
        iter_three = next(it)
        assert ("student1", {"view_grades", "view_classes"}) == iter_one
        assert ("teacher", {"view_grades", "change_grades", "add_grades", "delete_grades", "view_classes"}) == iter_three

class TestCsv:
    def test_csv(self) -> None:
        json_obj = Json(**{
            "student1": ["view_grades", "view_classes"],
            "student2": ["view_grades", "view_classes"],
            "teacher": ["view_grades", "change_grades", "add_grades", "delete_grades", "view_classes"]
        })
        csv_obj = Csv(json_obj)
        assert "student1" == csv_obj.rows[0][0]
        assert 1 == csv_obj.rows[0][1]
        assert "teacher" == csv_obj.rows[-1][0]

    def test_write(self) -> None:
        json_obj = Json(**{
            "student1": ["view_grades", "view_classes"],
            "student2": ["view_grades", "view_classes"],
            "teacher": ["view_grades", "change_grades", "add_grades", "delete_grades", "view_classes"]
        })
        csv_one = Csv(json_obj)
        csv_two = Csv(json_obj, delimiter='|')
        out_data_one = "person,view_grades,change_grades,add_grades," \
            + "delete_grades,view_classes,change_classes,add_classes," \
            + "delete_classes\r\nstudent1,1,0,0,0,1,0,0,0\r\n" \
            + "student2,1,0,0,0,1,0,0,0\r\nteacher,1,1,1,1,1,0,0,0\r\n"
        out_data_two = "person|view_grades|change_grades|add_grades|" \
            + "delete_grades|view_classes|change_classes|add_classes|" \
            + "delete_classes\r\nstudent1|1|0|0|0|1|0|0|0\r\n" \
            + "student2|1|0|0|0|1|0|0|0\r\nteacher|1|1|1|1|1|0|0|0\r\n"
        assert out_data_one == csv_one.write()
        assert out_data_two == csv_two.write()

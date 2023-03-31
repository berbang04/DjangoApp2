Contact_detail='''
    <!-- Forms start -->
<div class="col-sm-12">
    <form class="row g-3 p-4 m-3">
        <div class="col-6">
            <label for="inputEmail4" class="form-label">Email</label>
            <input type="email" class="form-control" id="inputEmail4">
        </div>
        <div class="col-6">
            <label for="inputPassword4" class="form-label">Password</label>
            <input type="password" class="form-control" id="inputPassword4">
        </div>
        <div class="col-6">
            <label for="inputAddress" class="form-label">Address</label>
            <input type="text" class="form-control" id="inputAddress" placeholder="Faruk erotik shop">
        </div>

        <div class="col-6">
            <label for="inputState" class="form-label">Bize nasıl ulaştiniz</label>
            <select id="inputState" class="form-select">
                <option selected>Choose...</option>
                <option>Facebook</option>
                <option>Instagram</option>
                <option>Twitter</option>
                <option>Github</option>
            </select>
        </div>

        <div class="col-12">
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="gridCheck">
                <label class="form-check-label" for="gridCheck">
                    Check me out
                </label>
            </div>
        </div>
        <div class="col-12">
            <button type="submit" class="btn btn-primary">Sign in</button>
        </div>
    </form>
</div>
<!-- Forms end -->
'''
About_detail='''

    <div class="container">
  <div class="h-100 p-5 bg-light border rounded-3">
    <h2>Add borders</h2>
    <p>Or, keep it light and add a border for some added definition to the boundaries of your content. Be sure to look
      under the hood at the source HTML here as we've adjusted the alignment and sizing of both column's content for
      equal-height.</p>
    <button class="btn btn-outline-secondary" type="button">Example button</button>
  </div>
  <!-- Next content ends -->
</div>
<!-- Hero content ends -->

'''

Fake_db_pages=[
    {"url":"contact","detail":Contact_detail,"title":"İletişim"},
    {"url":"about","detail":About_detail,"title":"Hakkımızda"},
    
]